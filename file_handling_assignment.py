file_handling_assignment.py
def create_and_write_file():
    my_file.txt('w')
    open('my_file.txt,'w')
         file.write("this text contains numbers./n")
         file.write("here are numbers:456789/n")
         file.write("and another line with number :234567/n")
         print("file created and initial content written sucessfully.")
         except IOError as e:
         print(f"An error occured whike creating/writing the file:{e}")
         
         def read_file():
         my_file.txt
         open('my_file.txt','r')as file:
         content=file.read()
         print("/nfile content:/n")
         print(content)
         exceptFileNotFoundError:
         print("file not found.please create the file first.")
         except IOError as e:
         print(f"An error occured while reading the file:{e}")

         def append_to_file():
         open('my_file.txt','a')
         file.write("This is an additional line 1./n")
         file.write("This is an additional line 2./n")
         file.write("This isn  an additional line 3./n")
         print("additional lines appended successfully.")
         exceptIOError as e:
         print(f"An error occured while appending to the file:{e}")


         def main():
         create_and_write_file()
         read_file()
         append_to_file()
         read_file()
         if_name_=="_main_":
         main()
