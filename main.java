import java.util.*;

public class Rock_Paper_Scissors {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		String choice[] = {"rock","paper","scissors"};
		System.out.println("Enter your choice (rock, paper, or scissors): ");
		String Human = sc.next().toLowerCase();
		String computer = choice [(int)(Math.random()*choice.length)];
		System.out.println("Computer chooses : "+computer);
		if(computer.equals("rock")&& Human.equals("paper") || computer.equals("paper")&& Human.equals("scissors") || 
				computer.equals("scissors")&& Human.equals("rock")) {
			System.out.println("Human wins!");
		}
		else if(computer.equals("paper")&& Human.equals("rock") || computer.equals("scissors")&& Human.equals("paper") || 
				computer.equals("rock")&& Human.equals("scissors")) {
			System.out.println("Computer Wins!");
		}
		else {
			System.out.println("Draw!");
		}
		

	}

}
