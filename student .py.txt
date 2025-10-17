
STUDENT MANAGEMENT SYSTEM
import java.util.ArrayList;

class Student {
    String name;
    int age;
    ArrayList<Integer> scores;

    Student(String name, int age, ArrayList<Integer> scores) {
        this.name = name;
        this.age = age;
        this.scores = scores;
    }

    double averageScore() {
        int sum = 0;
        for (int score : scores) sum += score;
        return sum * 1.0 / scores.size();
    }

    String grade() {
        double avg = averageScore();
        if(avg >= 90) return "A";
        if(avg >= 80) return "B";
        if(avg >= 70) return "C";
        if(avg >= 60) return "D";
        return "F";
    }
}

public class Main {
    public static void main(String[] args) {
        ArrayList<Integer> aliceScores = new ArrayList<>();
        aliceScores.add(95); aliceScores.add(88); aliceScores.add(92);

        ArrayList<Integer> bobScores = new ArrayList<>();
        bobScores.add(72); bobScores.add(65); bobScores.add(70);

        Student alice = new Student("Alice", 20, aliceScores);
        Student bob = new Student("Bob", 21, bobScores);

        Student[] students = {alice, bob};

        for(Student s : students) {
            System.out.println(s.name + " - Avg: " + s.averageScore() + " Grade: " + s.grade());
        }
    }
}



