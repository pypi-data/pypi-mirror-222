import sys

import os 
if not (os.path.dirname(os.path.abspath(__file__)).startswith(sys.path[-1])):
    import pytranslator, parser, header
    from errormanager import *
    from configmanager import *
    from util import *
else:
    from . import pytranslator, parser, header
    from .errormanager import *
    from .configmanager import *
    from .util import *



def cppcompile(r, file, pluscount=False):
  if file.endswith(".cpp") and os.environ.get("ENABLE_BETA_RPYC") == True:
    # compile the file to a file with the same name and path but .lua
    try:
      newctranslator = parser.CodeConverter(file, getconfig("c", "dynamiclibpath", "None"))
      newctranslator.parse(
      os.path.join(r, file),
      # C not C++
      flags=[
        '-I%s' % inc for inc in []
      ] + [
        '-D%s' % define for define in []
      ] + [
        '-std=%s' % getconfig("cpp", "std", "c++20")
      ] + [
        '-stdlib=%s' % getconfig("cpp", "stdlib", "libc++")
      ]
      )
      path = os.path.join(r, file)  
      newctranslator.diagnostics(sys.stderr)
      relative_path = backwordreplace(path,".cpp", ".lua", 1)
      with open(relative_path, 'w') as out:
        newctranslator.output(relative_path, out)   
                  
        #print(colortext.green("Compiled "+os.path.join(r, file)))
      if pluscount:
        pluscount.update(1)
        pluscount.current += 1
        #global count
        #count += 1
    except Exception as e:
      if "To provide a path to libclang use Config.set_library_path() or Config.set_library_file()" in str(e):
        print(error("dylib not found, use `roblox-pyc config`, c++, dynamiclibpath, and set the path to the dynamic library."))
      print(error(f"Compile Error!\n\n "+str(e), f"{os.path.join(r, file)}"))
      debug("Compiler error "+str(e))
      if pluscount:
        #pluscount.error()
        pluscount.update(1)
        pluscount.current += 1
        #global count
        #count += 1
        
        return 0      
  else:
    print(error("C is not enabled, please enable it in the config."))
    if pluscount:
      #pluscount.error()
      pluscount.update(1)
      pluscount.current += 1
      #global count
      #count += 1
      return 0
def ccompile(r, file, pluscount=False):
  if file.endswith(".c") and os.environ.get("ENABLE_BETA_RPYC") == True:
    # compile the file to a file with the same name and path but .lua
    try:
      newctranslator = parser.CodeConverter(file, getconfig("c", "dynamiclibpath", "None"))
      newctranslator.parse(
      os.path.join(r, file),
      # C not C++
      flags=[
        '-I%s' % inc for inc in []
      ] + [
        '-D%s' % define for define in []
      ] + [
        '-std=%s' % getconfig("c", "std", "c11")
      ] + [
        '-stdlib=%s' % getconfig("c", "stdlib", "libc")
      ]
      )
      path = os.path.join(r, file)  
                
      newctranslator.diagnostics(sys.stderr)
      relative_path = backwordreplace(path,".c", ".lua", 1)
      
      with open(relative_path, 'w') as out:
        newctranslator.output(relative_path, out)
                  
        #print(colortext.green("Compiled "+os.path.join(r, file)))
      if pluscount:
        pluscount.update(1)
        pluscount.current += 1
        #global count
        #count += 1
    except Exception as e:
      if "To provide a path to libclang use Config.set_library_path() or Config.set_library_file()" in str(e):
        print(error("dylib not found, use `roblox-pyc config`, c, dynamiclibpath, and set the path to the dynamic library."))
      print(error(f"Compile Error!\n\n "+str(e), f"{os.path.join(r, file)}"))
      debug("Compile error at "+str(e))
      if pluscount:
        #pluscount.error()
        pluscount.update(1)
        pluscount.current += 1
        #global count
        #count += 1
        return 0
  else:
    print(error("C is not enabled, please enable it in the config."))
    if pluscount:
      #pluscount.error()
      pluscount.update(1)
      pluscount.current += 1
      #global count
      #count += 1
      return 0
def pycompile(r, file, pluscount=False):
  # compile the file to a file with the same name and path but .lua
  contents = ""
            
  try:
    with open(os.path.join(r, file)) as rf:
      contents = rf.read()  
  except Exception as e:
    print(error(f"Failed to read {os.path.join(r, file)}!\n\n "+str(e)))
    # do not compile the file if it cannot be read
    return
            
  try:
    translator = pytranslator.Translator()
    lua_code = translator.translate(contents)
    #print(colortext.green("Compiled "+os.path.join(r, file)))
    # get the relative path of the file and replace .py with .lua
    path = os.path.join(r, file)  
      
    relative_path = backwordreplace(path,".py", ".lua", 1)
    
    if not os.path.exists(os.path.dirname(relative_path)):
      os.makedirs(os.path.dirname(relative_path))
    
    with open(relative_path, "w") as f:
      f.write(lua_code)
    
    if pluscount:
      #pluscount.error()
      pluscount.update(1)
      pluscount.current += 1
      #global count
      #count += 1
  except Exception as e:
    print(error(f"Compile Error!\n\n "+str(e), f"{os.path.join(r, file)}"))
    debug("Compile error at "+str(e))
    if pluscount:
      #pluscount.error()
      pluscount.update(1)
      pluscount.current += 1
      #global count
      #count += 1
      return 0
def lunarcompile(r, file, pluscount=False):
  # compile the file to a file with the same name and path but .lua
  # Run command and check if anything is outputted to stderr, stdout, or stdin
              
  process = subprocess.Popen(["moonc", os.path.join(r, file)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  stdout, stderr = process.communicate()
              
  if stdout or stderr:
    if stdout:     
      print(error(f"Compile Error!\n\n "+str(stdout), f"{os.path.join(r, file)}"))
      if pluscount:
        #pluscount.error()
        pluscount.update(1)
        pluscount.current += 1
        #global count
        #count += 1
        return 0
    else:
      print(error(f"Compile Error!\n\n "+str(stderr), f"{os.path.join(r, file)}"))
      if pluscount:
        #pluscount.error()
        pluscount.update(1)
        pluscount.current += 1
        #global count
        #count += 1
        return 0
  else:
    try:
      newheader = header.lunarheader([])
                  
      # check if the new file has been created
      if os.path.exists(os.path.join(r, file.replace(".moon", ".lua"))):
        #print(colortext.green("Compiled "+os.path.join(r, file)))          
        with open(os.path.join(r, file.replace(".moon", ".lua")), "r") as f:
          contents = f.read()
        contents = backwordreplace(contents, "return", "", 1)
        
      else:
        print(error("File error for "+os.path.join(r, file)+"!"))
      if pluscount:
        pluscount.update(1)
        pluscount.current += 1
        #global count
        #count += 1
    except Exception as e:
        print(error(f"Compile Error!\n\n "+str(e), f"{os.path.join(r, file)}"))
        
        if pluscount:
          #pluscount.error()
          pluscount.update(1)
          pluscount.current += 1
          #global count
          #count += 1
          return 0
def robloxtscompile(r, file, pluscount=False):
  # Just add to pluscount, add later
  try:
    print(warn("At the moment roblox-ts is not supported, please wait for a future update."))
    if pluscount:
      #pluscount.error()
      pluscount.update(1)
      pluscount.current += 1
      #global count
      #count += 1
  except Exception as e:
      print(error(f"Compile Error!\n\n "+str(e), f"{os.path.join(r, file)}"))
      if pluscount:
        #pluscount.error()
        pluscount.update(1)
        pluscount.current += 1
        #global count
        #count += 1
        return 0
def allcompile(r, file, pluscount):
  # Checks what file it is then redirects to the correct compiler
  if file.endswith(".py"):
    pycompile(r, file, pluscount)
  elif file.endswith(".moon"):
    lunarcompile(r, file, pluscount)
  elif file.endswith(".c"): 
    ccompile(r, file, pluscount)
  elif file.endswith(".cpp"):
    cppcompile(r, file, pluscount)
  elif file.endswith(".ts"):
    robloxtscompile(r, file, pluscount)
  