import json
import openai
import pinecone
import datetime
import traceback
import pandas as pd
from flask import request
import loggerutility as logger
import commonutility as common
from openai.embeddings_utils import get_embedding, get_embeddings, cosine_similarity


class OpenAI_PineConeVector:
    
    index_name      =   ""
    openAI_apiKey   =   ""
    pineCone_apiKey =   ""
    queryList       =   "" 
    dfJson          =   ""
    engineName      =   "text-embedding-ada-002" # Model that we want to use 
    dimensions      =   1536
    my_index        =   ""
    enterpriseName  =   ""
    modelScope      =   "E"
    
    def trainData(self, pineCone_json):
        # When calling from process definition, we need to pass hard-coded openAI_apiKey & pineCone_apiKey.
        try:
            
            result  = ""
            logger.log("inside PineConeVector class trainData()","0")
            if "openAI_apiKey" in pineCone_json and pineCone_json["openAI_apiKey"] != None:
                self.openAI_apiKey = pineCone_json["openAI_apiKey"]           
                logger.log(f"\ntrain_PineConeVector openAI_apiKey:::\t{self.openAI_apiKey} \t{type(self.openAI_apiKey)}","0")
            
            if "pineCone_apiKey" in pineCone_json and pineCone_json["pineCone_apiKey"] != None:
                self.pineCone_apiKey = pineCone_json["pineCone_apiKey"]           
                logger.log(f"\ntrain_PineConeVector pineCone_apiKey:::\t{self.pineCone_apiKey} \t{type(self.pineCone_apiKey)}","0")

            if "modelParameter" in pineCone_json and pineCone_json["modelParameter"] != None:
                self.modelParameter = json.loads(pineCone_json['modelParameter'])
            
            if "index_name" in self.modelParameter and self.modelParameter["index_name"] != None:
                self.index_name = self.modelParameter["index_name"]
                logger.log(f"\ntrain_PineConeVector index_name:::\t{self.index_name} \t{type(self.index_name)}","0")
            
            if "modelJsonData" in pineCone_json and pineCone_json["modelJsonData"] != None:
                self.dfJson = pineCone_json["modelJsonData"]
                logger.log(f"\ntrain_PineConeVector dfJson:::\t{self.dfJson} \t{type(self.dfJson)}","0")
            
            if "enterprise" in pineCone_json and pineCone_json["enterprise"] != None:
                self.enterpriseName = pineCone_json["enterprise"]
                logger.log(f"\nPineConeVector class TrainData enterprise:::\t{self.enterpriseName} \t{type(self.enterpriseName)}","0")

            if "modelScope" in pineCone_json and pineCone_json["modelScope"] != None:
                self.modelScope = pineCone_json["modelScope"]
                logger.log(f"\nPineConeVector class TrainData modelScope:::\t{self.modelScope} \t{type(self.modelScope)}","0")


            
            if type(self.dfJson) == str :
                parsed_json = json.loads(self.dfJson)
                if self.index_name == 'item':
                    df = pd.DataFrame(parsed_json[1:])  # Added because actual data values start from '1' position
                elif self.index_name == 'document':
                    df = pd.DataFrame(parsed_json)      # Added because actual data values start from '0' position
            else:
                df = pd.DataFrame(self.dfJson)
                
            logger.log(f"Pinecone Available indexes List df :: \t {df}", "0")    
            pinecone.init(api_key=self.pineCone_apiKey, environment='us-west4-gcp')
            openai.api_key = self.openAI_apiKey                 

            logger.log(f"Pinecone Available indexes List  :: \t {pinecone.list_indexes()}", "0")    
            # Creating index
            if self.index_name not in pinecone.list_indexes():
                logger.log(f" \n'{self.index_name}' index not present. Creating New!!!\n", "0")
                pinecone.create_index(name = self.index_name, dimension=self.dimensions, metric='cosine')
                self.my_index = pinecone.Index(index_name=self.index_name)
            else:
                logger.log(f" \n'{self.index_name}' index is present. Loading now!!!\n", "0")
                self.my_index = pinecone.Index(index_name=self.index_name)
            logger.log(f"Pinecone Available indexes List  :: \t {pinecone.list_indexes()}", "0")    

            df.columns = ['_'.join(column.lower().split(' ')) for column in df.columns]
            df.fillna("N/A",inplace=True)
            #Changing column names to lowercase and replacing nan values with a string placeholder
            df.columns = ['_'.join(column.lower().split(' ')) for column in df.columns]
            df.fillna("N/A",inplace=True)
            
            if self.modelScope == "G" :
                self.enterpriseName = ""
            
            df['enterprise'] = self.enterpriseName
            
            if self.index_name == "item":
                logger.log(f"\ntrain_PineConeVector df.head() line 84:: {df.head()},\n {df.head()}", "0")    
                df.columns = ['id', 'material_description', 'product', 'delivery_method', 'strength', 'size', 'enterprise']
                logger.log(f"\ntrain_PineConeVector df.head() line 86:: {df.head()},\n {df.head()}", "0")    
                df['embedding'] = get_embeddings(df['material_description'].to_list(), engine=self.engineName)
                metadata = df[['material_description', 'product', 'delivery_method', 'strength', 'size', 'enterprise']].to_dict(orient='records')
            
            elif self.index_name == "document":
                df['embedding'] = get_embeddings(df['description'].to_list(), engine=self.engineName)
                metadata = df[['description','enterprise']].to_dict(orient='records')

            else:
                logger.log(f"\n\n INVALID INDEX NAME ::: \t{self.index_name}\n", "0")    
            
            upsert = list(zip(df['id'], df['embedding'], metadata))
            _ = self.my_index.upsert(vectors=upsert)
            logger.log(f"{self.my_index.describe_index_stats()}","0")

            logger.log(f"\nOpenAI_PineConeVector class trainData:::\t{self.my_index}","0")
            result = f" '{self.index_name}' Index Creation SUCCESSFUL for Enterprise: '{self.enterpriseName}'. "
            logger.log(f"\nOpenAI_PineConeVector class trainData Result:::{result}\n","0")
            return result
            
        except Exception as e:
            logger.log(f" '{self.index_name}' Index Creation FAILED for Enterprise: '{self.enterpriseName}'. ","0")
            logger.log(f"OpenAI_PineConeVector class trainData() Issue::: \n{e}","0")
            trace = traceback.format_exc()
            descr = str(e)
            errorXml = common.getErrorXml(descr, trace)
            logger.log(f'\n OpenAI_PineConeVector class trainData() errorXml::: \n{errorXml}', "0")
            return str(errorXml)

    def getLookupData(self):               
        try:
            
            logger.log("inside PineConeVector class LookUpData()","0")
            result            = []
            id_list           = []
            finalResult       = {}
            queryJson_keyList = []
            queryJson         = ""
            
            pineCone_json =  request.get_data('jsonData', None)
            pineCone_json = json.loads(pineCone_json[9:])
            logger.log(f"\nPineConeVector class getLookupData() pineCone_json:::\t{pineCone_json} \t{type(pineCone_json)}","0")

            if "openAI_apiKey" in pineCone_json and pineCone_json["openAI_apiKey"] != None:
                self.openAI_apiKey = pineCone_json["openAI_apiKey"]          
                logger.log(f"\nPineConeVector class LookUpData() openAI_apiKey:::\t{self.openAI_apiKey} \t{type(self.openAI_apiKey)}","0")
                openai.api_key = self.openAI_apiKey                 

            if "pineCone_apiKey" in pineCone_json and pineCone_json["pineCone_apiKey"] != None:
                self.pineCone_apiKey = pineCone_json["pineCone_apiKey"]           
                logger.log(f"\nPineConeVector class LookUpData() pineCone_apiKey:::\t{self.pineCone_apiKey} \t{type(self.pineCone_apiKey)}","0")

            if "index_name" in pineCone_json and pineCone_json["index_name"] != None:
                self.index_name = pineCone_json["index_name"]
                logger.log(f"\nPineConeVector class LookUpData() index_name:::\t{self.index_name} \t{type(self.index_name)}","0")
            
            if "queryJson" in pineCone_json and pineCone_json["queryJson"] != None:
                queryJson = pineCone_json["queryJson"]
                logger.log(f"\nPineConeVector class LookUpData() queryJson:::\t{queryJson} \t{type(queryJson)}","0")
            
            if "enterprise" in pineCone_json and pineCone_json["enterprise"] != None:
                self.enterpriseName = pineCone_json["enterprise"]
                logger.log(f"\nPineConeVector class LookUpData() enterprise:::\t{self.enterpriseName} \t{type(self.enterpriseName)}","0")

            if "modelScope" in pineCone_json and pineCone_json["modelScope"] != None:
                self.modelScope = pineCone_json["modelScope"]
                logger.log(f"\nPineConeVector class LookUpData() modelScope:::\t{self.modelScope} \t{type(self.modelScope)}","0")

            if self.modelScope == "G":
                self.enterpriseName = ""

            openai.api_key  =  self.openAI_apiKey         
            pinecone.init(api_key=self.pineCone_apiKey, environment='us-west4-gcp')
            queryJson_keyList = list(queryJson.keys())
            self.queryList = list(queryJson.values())
            
            pinecone_IndexList = pinecone.list_indexes()
            
            if self.index_name in pinecone_IndexList:
                self.my_index = pinecone.Index(index_name=self.index_name)
                logger.log(f"self.my_index::: {self.my_index}","0")
                logger.log(f"Pinecone execution START Time::: {datetime.datetime.now().strftime('%H:%M:%S')}","0")
                for query in self.queryList:
                    if len(query) > 0 :
                        if self.index_name == 'item':
                            result.append(self.my_index.query(vector=get_embedding(query, engine=self.engineName),filter={"enterprise": self.enterpriseName},top_k=1, include_metadata=True))
                        else:
                            pineConeResponse = self.my_index.query(vector=get_embedding(query, engine=self.engineName),filter={"enterprise": self.enterpriseName},top_k=10, include_metadata=True)
                            result.append(pineConeResponse)
                    else:
                        logger.log(f"\n Description with {len(query)} character length found:::'{query}' in queryList \n", "0")

                logger.log(f"Pinecone execution END Time::: {datetime.datetime.now().strftime('%H:%M:%S')}","0")
                logger.log(f"OpenAI_PineConeVector class getLookUP() Response::: \n{result}\tlen::: {len(result)}\t{type(result)}", "0")
                
                # filtering response 
                if len(result[0]['matches']) > 0:
                    if self.index_name == 'item':
                        pineconeId_list = [element["matches"][0]["id"] for element in result]
                        pineconeDescription_list = [element["matches"][0]["metadata"]["material_description"] for element in result] 
                        for i in range(len(queryJson_keyList)):
                            finalResult[queryJson_keyList[i]] = {"material_description": pineconeDescription_list[i], "id": pineconeId_list[i]}
                        logger.log(f"\n\nOpenAI_PineConeVector class getLookUP() 'ITEM' Index finalResult ::: \n{finalResult}\tlen::: {len(finalResult)}\t{type(finalResult)}", "0")
                    else :
                        logger.log(f"\n\nOpenAI_PineConeVector class getLookUP() 'DOCUMENT' Index result::: \n{result}\tlen::: {len(result)}\t{type(result)}", "0")
                        for query in self.queryList:
                            for matchJson in result:
                                # logger.log(f"\n\nOpenAI_PineConeVector class getLookUP() 'DOCUMENT' Index matchJson::: \n{matchJson}\t{type(matchJson)}", "0")
                                for j in matchJson['matches']:
                                    # logger.log(f"\n\nOpenAI_PineConeVector class getLookUP() 'DOCUMENT' Index j::: \n{j}\t{type(j)}", "0")
                                    if j['score']  >= 0.75 and query in j['metadata']['description']:
                                        id_list = [k['id'] for k in matchJson['matches']]
                        logger.log(f"\n\nOpenAI_PineConeVector class getLookUP() 'DOCUMENT' Index id_list::: \n{id_list}\t\t{type(id_list)}", "0")
                        finalResult = id_list
                return str(finalResult)
            
            else:
                logger.log(f"OpenAI_PineConeVector class getLookUP()::: \nIndex_Name: {self.index_name} not found in pinecone_IndexList: {pinecone_IndexList}","0")
                message = f"Index_Name: '{self.index_name}' not found in pinecone_IndexList: {pinecone_IndexList}"
                errorXml = common.getErrorXml(message, "")
                raise Exception(errorXml)
            
        except Exception as e:
            logger.log(f"OpenAI_PineConeVector class getLookUP() Issue::: \n{e}","0")
            trace = traceback.format_exc()
            descr = str(e)
            errorXml = common.getErrorXml(descr, trace)
            logger.log(f'\n OpenAI_PineConeVector class getLookUP() errorXml::: \n{errorXml}', "0")
            return str(errorXml)





