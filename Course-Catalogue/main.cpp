#include<iostream>
#include <string>
#include <string.h>

using namespace std;


struct Course{

    char* Name;

    Course(){
        this->Name = nullptr;
    }

    Course(const Course& other){
        if(other.Name != nullptr){
            Name = new char[strlen(other.Name) + 1]; //takes the name of the other course and set this names length to that
            strcpy(Name, other.Name); //constructor that takes the name of the other and applies it to the course being made
        }
        else{
            this->Name = nullptr;
        }
    }

    void ChangeName(const char* p){
        delete[] this->Name;
        Name = new char [strlen(p) + 1];
        strcpy(this->Name,p);
    }

    Course& operator=(const Course& other) {
        if (this != &other) {
            delete[] Name;

            if (other.Name != nullptr){
                Name = new char[strlen(other.Name) + 1];
                strcpy(Name, other.Name);
            } else {
                Name = nullptr;
            }
        }
        return *this;
    }

    ~Course(){
        delete[] Name;
    }
    // add in current grade, assignments, and other useful tools, the end goal is to retrieve marks and display projected grades
};

struct CourseList{

    int size;
    int length ;
    Course* courses;

    CourseList(int size){
        this->size = size;
        length = 0;
        courses = new Course[size];
    }

    void ExpandLength(){

        size = size*2;
        Course* NewCourseList = new Course[size];

        for(int i = 0; i < length; i++){
            NewCourseList[i] = courses[i];  
        }

        delete[] courses;
        courses = NewCourseList;
    }

    void AddCourse(Course& input){
        if (length >= size){
            ExpandLength();
        }
        courses[length] = input;
        length++;
    }

    ~CourseList(){
        delete[] courses;
    }
};



int main(){

    cout<<"---COURSE-CATALOG---"<<endl;
    cout<<"Welcome, Please Input The number of courses you have this semester"<<endl;
    cout<<"COURSE COUNT: ";
    int CourseCount;

    while(true){
        cin>>CourseCount;
        if(cin.fail() || CourseCount <= 0){
            cout<<"Error: Input was not of type Int OR <= 0" <<endl;
            cout<<"COURSE COUNT: ";

            cin.clear();
            cin.ignore(1000,'\n');
        }
        else{
            break;
        }
    }

    CourseList Catalog(CourseCount);

    cout<<"Add the Names of your Courses"<<endl;

    for(int i = 0; i < CourseCount; i++){
        //CURRENTLY NEEDS FIXING///////////////////////////////////////////////////////////////////
        char input[100];
        cout<<"COURSE"<<i+1<<": ";
        cin.getline(input, 100);
        ////////////////////////////////////////////////////////////////////////////////////////////
        Course temporary;
        Catalog.AddCourse(temporary);

        cout<<endl;
    }
    for(int i = 0; i < CourseCount; i++){
        cout << "COURSE" << i+1 << ": " <<Catalog.courses[i].Name <<endl;
    }
    
    return 0;
}
