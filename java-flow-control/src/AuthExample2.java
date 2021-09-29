
public class AuthExample2 {

	public static void main(String[] args) {
		String[][] users = {
				{"eric","790216"},
				{"minwoo","790728"},
				{"dongwan","791121"},
				{"hyesung","791127"},
				{"jin","800819"},
				{"andy","810121"}
		};
		String inputId = args[0];
		String inputPw = args[1];
		
		boolean isLogined = false;
		for(int i=0; i<users.length; i++) {
			if(
					users[i][0].equals(inputId) &&
					users[i][1].equals(inputPw)
					) {
				isLogined = true;
				break;				
			}				
		}
		if(isLogined) {
			System.out.println("Welcome!! "+args[0]);
		} else {
			System.out.println("Check your ID and Password.");
		}
	}

}
