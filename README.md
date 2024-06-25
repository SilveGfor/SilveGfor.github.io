#include <iostream>
#include <vector>
#include <string>
#include <stdexcept> // Для std::out_of_range исключения

class Teacher {
public:
    Teacher(const std::string& name) : _name(name) {}
    virtual ~Teacher() {}

    const std::string& getName() const { return _name; }
    virtual double calcWages() const = 0;

protected:
    std::string _name;
};

class AssociateTeacher : public Teacher {
public:
    AssociateTeacher(const std::string& name, int bonus) : Teacher(name), _bonus(bonus) {}

    static const int BASE_SALARY = 1500;

    double calcWages() const override {
        return BASE_SALARY + _bonus;
    }

    int getBonus() const { return _bonus; }

private:
    int _bonus;
};

class InvitedTeacher : public Teacher {
public:
    InvitedTeacher(const std::string& name, int stuGroups) : Teacher(name), _stuGroups(stuGroups) {}

    static const int GROUP_TAX = 2000;

    double calcWages() const override {
        return GROUP_TAX + _stuGroups * 100; // Предположим, что _stuGroups влияет на расчет зарплаты
    }

    int getStuGroups() const { return _stuGroups; }

private:
    int _stuGroups;
};

class TArray {
public:
    ~TArray() {
        for (Teacher* teacher : _arr) {
            delete teacher;
        }
    }

    size_t getSize() const {
        return _arr.size();
    }

    AssociateTeacher* addAssociateTeacher(const std::string& name, int bonus) {
        AssociateTeacher* teacher = new AssociateTeacher(name, bonus);
        _arr.push_back(teacher);
        return teacher;
    }

    InvitedTeacher* addInvitedTeacher(const std::string& name, int stuGroups) {
        InvitedTeacher* teacher = new InvitedTeacher(name, stuGroups);
        _arr.push_back(teacher);
        return teacher;
    }

    std::pair<int, int> totalWagesOfTopTeachers(int minGroups, int minBonus) const {
        int totalAssociateWages = 0;
        int totalInvitedWages = 0;

        for (const Teacher* teacher : _arr) {
            if (const AssociateTeacher* assocTeacher = dynamic_cast<const AssociateTeacher*>(teacher)) {
                if (assocTeacher->getBonus() >= minBonus) {
                    totalAssociateWages += assocTeacher->calcWages();
                }
            } else if (const InvitedTeacher* invitedTeacher = dynamic_cast<const InvitedTeacher*>(teacher)) {
                if (invitedTeacher->getStuGroups() >= minGroups) {
                    totalInvitedWages += invitedTeacher->calcWages();
                }
            }
        }

        return std::make_pair(totalAssociateWages, totalInvitedWages);
    }

    // Перегрузка оператора []
    Teacher* operator[](size_t index) {
        if (index >= _arr.size()) {
            throw std::out_of_range("Index out of range");
        }
        return _arr[index];
    }

    const Teacher* operator[](size_t index) const {
        if (index >= _arr.size()) {
            throw std::out_of_range("Index out of range");
        }
        return _arr[index];
    }

    friend std::ostream& operator << (std::ostream& os, const TArray& tArr);

protected:
    std::vector<Teacher*> _arr;
};

std::ostream& operator << (std::ostream& os, const TArray& tArr) {
    for (const Teacher* teacher : tArr._arr) {
        os << teacher->getName() << " earns " << teacher->calcWages() << std::endl;
    }
    return os;
}

int main() {
    TArray tArr;
    tArr.addAssociateTeacher("Sam Sawyer", 1000);
    tArr.addAssociateTeacher("Emily Stone", 2000);
    tArr.addInvitedTeacher("John Caine", 3);
    tArr.addInvitedTeacher("Alice Johnson", 5);

    std::cout << "Teachers:" << std::endl;
    for (size_t i = 0; i < tArr.getSize(); ++i) {
        std::cout << "[" << i << "] " << tArr[i]->getName() << std::endl;
    }

    try {
        std::cout << "First teacher's wages: " << tArr[0]->calcWages() << std::endl;
    } catch (const std::out_of_range& e) {
        std::cerr << "Exception: " << e.what() << std::endl;
    }

    // Деструктор TArray автоматически вызовется здесь и освободит память

    return 0;
}
