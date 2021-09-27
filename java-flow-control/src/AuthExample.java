
public class AuthExample {

	public static void main(String[] args) {
		String id = "ketty";
		String pw = "1234";
		String inputId = args[0];
		String inputPw = args[1];
		
		if(inputId.equals(id) && inputPw.equals(pw)) {
			System.out.println("Hello "+ args[0]);
		} else {
			System.out.println("check your id and password");
		}
		

	}

}
