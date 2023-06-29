from oop import Course, Student

math = Course("Math", "Mr. E")
english = Course("English", "Mr. E")
science = Course("Science", "Mr. E")

bob = Student("Bob", 10, [math, english, science])
bob.list_courses()