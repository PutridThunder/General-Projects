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

    Course& operator=(const Course& other) {
        if (this != &other) {
            delete[] Name;

            Name = new char[strlen(other.Name) + 1];
            strcpy(Name, other.Name);
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

    CourseList(const int size){
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

    ~CourseList(){
        delete[] courses;
    }
};


void Add_Course(char*& name){
    //use this to add courses to course list
    return;
}


int main(){

    while (true){



    }




    return 0;
}
