/**
* driver for hw05 hash tables
*
* see comment in the parse loop
*
* @author Austin Leithner
* @version 10/9/19
*
*/
import java.util.*;
import java.io.*;
public class Driver{
   public static void main(String[] args)throws FileNotFoundException{
   
      int wordsChecked =0;
      int wordsMispelled=0;
      Timer totalTime = new Timer();
      Timer loadTime = new Timer();
      Timer parseTime = new Timer();
      totalTime.start();
      loadTime.start();
   
      DictHash dictionary = new DictHash("../data/dictionary.txt");
      PhonHash phonDictionary = new PhonHash("../data/dictionary.txt");
      loadTime.stop();
      
      int i;
      String [] splitted;
      //Scanner f;
      String str;
      Scanner fiq = new Scanner(new File("../data/melville.txt"));
      parseTime.start();
      while(fiq.hasNextLine()==true){
         //System.out.println(fiq.nextLine());
         
         // inside loop where I'm reading from melville.txt
         str= fiq.nextLine();
         str= str.replaceAll("[^a-zA-Z]", " "); // get rid of non-alphanumeric
         splitted = str.split("\\s+");          // split based on whitespace
         for (i=0; i<splitted.length; i++) {
            if (splitted[i].length() > 2 && !splitted[i].matches(".*[A-Z].*")) {
               // we have extracted a "word" (splitted[i]) from melville.txt
               // this word contains only lowercase letters and is more than 2 characters
               //System.out.println(splitted[i]);
               wordsChecked ++;
               Metaphone3 m3 = new Metaphone3();
               String phon;
               m3.SetWord(splitted[i]);
		         m3.Encode();
		         phon = m3.GetMetaph();
               
               DictWord tempDictWord= new DictWord(splitted[i],phon);
               
               if(!(dictionary.isInDict(tempDictWord))){
                  //System.out.println(splitted[i]);
                  
                  System.out.print("Suggestions for " +splitted[i]+ ": ");
                  /*
                  So um this program dosen't output the same thing as hw01 it might be because of the findPhon method
                  I have spent a very long time trying to find out why this doesn't work. It seams that it should work
                  but it doesn't. It has the same word count as hw01 so I know that isindict, hash ,and add works.
                  
                  Edit: The issue was cause by mot setting an encode value after initializing the Metaphone3 object
                  see DemoMetaphone3 line 37.
                  
                  */
                  phonDictionary.findPhon(tempDictWord);
                  System.out.println();
                  wordsMispelled++;
               }
               
            }
         }  
      }
      parseTime.stop();
      totalTime.stop();
      
      
      
      System.out.println("Words in Dictionary: "+dictionary.getTotalWords());
      System.out.println("Words Checked      : "+wordsChecked);
      System.out.println("Words Not Found    : "+wordsMispelled);
      System.out.println("Time Spent Loading : "+loadTime.seconds() +" seconds");
      System.out.println("Time Spent Parsing : "+parseTime.seconds() +" seconds");
      System.out.println("Total Time Spent   : "+totalTime.seconds() +" seconds");
      System.out.println("longest list in dictionary       : "+dictionary.longestList());
      System.out.println("longest list in phonDictionary   : "+phonDictionary.longestList());
      System.out.println("number of elems in dictionary    : "+dictionary.totalElems());
      System.out.println("number of elems in phonDictionary: "+phonDictionary.totalElems());
      
   }
}