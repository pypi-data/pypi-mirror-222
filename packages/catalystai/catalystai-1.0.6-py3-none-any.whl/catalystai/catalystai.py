
import psycopg2
import psycopg2.extras
from minio import Minio
from io import BytesIO
import pandas as pd
import datetime

class Add_file:
    
    def __init__(self,email,workspace_id,project_id,data,filename):
        self.email = email
        self.workspace_id = workspace_id #202ff3a7-8644-471a-9cc0-4b882780f673
        self.project_id = project_id  #467dd3c1-2468-4b66-9aba-8072e3124582
        self.data = data
        self.filename = filename
#         self.filetype = filetype
    
#     @classmethod
    def add_data(self):
        user_id =  self.Validate_user()
        minio_client = self.Connect_minio()
        return_data = self.add_minio_data(minio_client,user_id)
        splitreturndata = return_data.object_name.split("/")
        print("Data added as {0} ".format(splitreturndata[len(splitreturndata)-1]))
        
    def Validate_user(self):
        conn = psycopg2.connect("dbname=%s user=%s host=%s password=%s" % ("postgres","master","dpg-cj29e6liuie55pg7jjk0-a.singapore-postgres.render.com","x77DG0cIoNvpd3KNmvZdqV2RK3197On1"))
        cursor = conn.cursor()
        # print("Connected to Database")
        query = "SELECT user_id from t_user where email = '%s' and is_active = true " %(self.email)
        try :
            cursor.execute(query)
            result = cursor.fetchone()
            # print("User ID: ",result[0])
            
            if result:
                return result[0]
            else:
                return "User {} does not exist in the database".format(self.email) 
#                 print("User {} does not exist in the database".format(self.email))
            
        except Exception as e:
            return e
        finally:
            conn.commit()
            conn.close()
           
    def Connect_minio(self):
        try :
            minio_client = Minio(
            "storage.catalystlabs.ai:9000",
            access_key = "HBbMqITM5SAv6MbnU18N",
            secret_key = "O7LWGjCks8TltKK5CCXOCJ5yg8sEciclvlSkrXQR",
            secure=True,
            )
            # print("Connected to MinIO")
            return minio_client
        except Exception as e:
            return e
#             print(e)
            
    def add_minio_data(self,minio_client,user_id):
        try:
            
            csv_bytes = self.data.to_csv().encode('utf-8')
            csv_buffer = BytesIO(csv_bytes)
            current_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
            object_name = str(self.workspace_id) +"/"+str(self.project_id)+"/data-files/"+str(current_time)+"/"+str(self.filename)
            found = minio_client.bucket_exists(str(user_id))
            if not found:
                try :
                    minio_client.make_bucket(str(user_id))
                    result = minio_client.put_object(user_id,object_name,csv_buffer,length=-1)
                    return result
                except Exception as e:
                    return e
            
            else:
                try:
                    result = minio_client.put_object(user_id,object_name,csv_buffer,length=len(csv_bytes))
                    return result
                except Exception as e:
                    return e
        except Exception as e:
            return e
