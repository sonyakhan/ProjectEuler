public class Interest {
	public static void main(String[] args)
	{

		double owed = 1000.0;
		double currentInterestRate = 0.20;
		double interestRateIncrease = 1.05;
		int numberOfMonths = 0;


		while(owed < 12000)
		{
			owed = owed + (owed * currentInterestRate);
			currentInterestRate = interestRateIncrease * currentInterestRate;
			numberOfMonths++;
		}
		
		System.out.println(owed);

	}
}