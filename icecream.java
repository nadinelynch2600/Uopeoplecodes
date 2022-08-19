package text.io;
public class icecream { 
public static void main(String args[]){

	//Read the icecream file
	TextIO.readFile("icecream.dat");

	double strawberrysold = 0; //Counter to keep track of how many strawberrys were sold
	double conescount = 0; //Counter to keep track of all the cones sols

	//While we have not reached end of file
	while(TextIO.eof() == false){

	conescount = conescount + 1; //Every line is a cone, so add each line to the counter

	String icecreamFlavour = TextIO.getlnString(); //Get the name of the icecream
	if(icecreamFlavour.equals("Strawberry")){ //If name is strawberry
	strawberrysold = strawberrysold + 1; //Add to the straberry counter.
	}
	}

	System.out.println("Stawberry Falvour Sold: "+ strawberrysold);
	System.out.println("Total Cones Sold: "+ conescount);
	System.out.println("% of cones that are strawberry: "+ (strawberrysold/conescount)*100);
	}