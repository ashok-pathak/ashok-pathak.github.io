from cx_Freeze import setup, Executable 
  
setup(name = "Writer" , 
      version = "0.1" , 
      description = "" , 
      executables = [Executable("writer.py")]) 
