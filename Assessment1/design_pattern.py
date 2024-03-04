
class Language():
    def Write(self):
        pass

class Python(Language):
    dynamic = True
    
    def Write(self):
        print("Writing python code")

class CSharp(Language):
    dynamic = False
    def Write(self):
        print("Writing cSharp code")

class Basic(Language):
    dynamic = False
    
    def Write(self):
        print("writing basic")

class ProgrammingLanguages():
    def CreateLanguage(name):
        if name == "python":
            return Python()
        if name == "csharp":
            return CSharp()
        if name == "basic":
            return Basic()
    
language1 = ProgrammingLanguages.CreateLanguage("csharp")
language1.Write()

if language1.dynamic:
    print("This language is dynamic")
else:
    print("this language is not dynamic")