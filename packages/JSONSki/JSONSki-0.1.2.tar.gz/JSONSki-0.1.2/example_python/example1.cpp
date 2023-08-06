

#include "../src/QueryAutomaton.h"

#include "../src/JSONPathParser.h"
#include "../src/JSONPathParser.cpp"



#include "../src/Records.h"

#include "../src/RecordLoader.h"
#include "../src/RecordLoader.cpp"


#include "../src/QueryProcessor.h"
#include "../src/QueryProcessor.cpp"
#include <pybind11/pybind11.h>




std::string execute_query(const char* input) {
// std::string execute_query(char* input) {
//int main(){
 // char* file_path = "../dataset/twitter_sample_large_record.json";
 // const char* file_path = "../dataset/twitter_sample_large_record.json";
    cout<<"start loading the single large record from "<<input<<endl;
    Record* rec = RecordLoader::loadSingleRecord(input);
    if (rec == NULL) {
        cout<<"record loading fails."<<endl;
        return "record loading fails";
    }
    cout<<"finish loading the single large record"<<endl;

    string query = "$[*].entities.urls[*].url";
    cout<<"\nstart executing query "<<query<<endl;
    QueryProcessor processor(query);
    string output = processor.runQuery(rec);
    cout<<"finish query execution"<<endl;
    cout<<"matches are: "<<output<<endl;
    return output;
}

 std::string execute_query(const char* input);
 
// std::string execute_query(char* input);

PYBIND11_MODULE(JSONSki, handle) {
    handle.doc() = "This is just a demo";
    handle.def("execute_query", &execute_query, "Function to execute the query and return the matches");
}

