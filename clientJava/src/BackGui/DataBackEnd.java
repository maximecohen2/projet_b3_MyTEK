package BackGui;

public abstract class DataBackEnd {
	private static String myToken;

	public static String getMyToken() {
		return myToken;
	}

	public static void setMyToken(String token) {
		myToken = token;
	}
}
