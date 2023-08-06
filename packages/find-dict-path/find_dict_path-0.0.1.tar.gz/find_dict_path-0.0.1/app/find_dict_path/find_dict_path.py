from typing import List


class Find_Dict_Path:
    
    def __init__(self) -> None:
        self.ans=[]


    def get_full_path(self,raw_dict_list_data:dict,search_key_name:str,find_first_occurance:bool=True) -> str:
        self.ans=[]
        self.__find_full_path_of_key(raw_dict_list_data,search_key_name,find_first_occurance)        
        return self.__get_path_formatter()
        
    def __get_path_formatter(self) -> str:
        
        if self.ans==[]:
            return "[]"
        
        formatted_path=""
        
        for sub_path in self.ans:
            if isinstance(sub_path,int) or sub_path=="*":
                formatted_path+=f"[{sub_path}]"
            else:
                formatted_path+=f"['{sub_path}']"
                
        return formatted_path
    
    def __find_full_path_of_key(self,raw_dict_list_data:dict,search_key_name:str,find_first_occurance:bool=True) -> bool:
        
        if isinstance(raw_dict_list_data,list):
            for index,single_list_data in enumerate(raw_dict_list_data):
                result=self.__find_full_path_of_key(single_list_data,search_key_name,find_first_occurance)
                if result:
                        self.ans.insert(0,index if find_first_occurance else "*")
                        return True
                
        if isinstance(raw_dict_list_data,dict):
            for key,value in raw_dict_list_data.items():
                if key==search_key_name:
                    self.ans.insert(0,key)
                    return True
                else:
                    result=self.__find_full_path_of_key(value,search_key_name,find_first_occurance)
                    if result:
                        self.ans.insert(0,key)
                        return True
                        
        return False
    
    