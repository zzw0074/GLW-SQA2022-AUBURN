from attack_model import calculate_k,  perform_inference
from py_parser import getPythonParseObject, getImport, getFunctionAssignments

def fuzz_1():
    y_test = "2"
    calculate_k(2,3,5,y_test)
    print('='*100)

def fuzz_2():
    model_name = "KNeighbors"
    perform_inference(2,3,5,7,model_name)
    print('='*100)

def fuzz_3():
    pyFile = "C:\Users\&7\Desktop\TestOrchestrator4ML-main\generation"
    getPythonParseObject(pyFile)
    print('='*100)

def fuzz_4():
    pyTree = "!@#$%^&*()`~"
    getImport(pyTree)
    print('='*100)

def fuzz_5():
    class_body = "-9223372036854775808/-1"
    getFunctionAssignments(class_body)
    print('='*100)

if __name__=='__main__':
    fuzz_1()
    fuzz_2()
    fuzz_3()
    fuzz_4()
    fuzz_5()