/*
* Reads from a dictionary file and spellchecks the provided text file
* This is the driver class
*
* Author: Austin Leithner
* Version: 8/30/19
*
*/

import java.util.*;
import java.io.*;

public class DemoMetaphone3
{
	public static void main(String[] args) throws FileNotFoundException
	{
		
		//Scanner kb= new Scanner(System.in);
      
      
      DictList dictionary = new DictList();
      
      int totalWords =0;
      int wordsChecked =0;
      int wordsMispelled=0;
      Timer totalTime = new Timer();
      Timer loadTime = new Timer();
      Timer parseTime = new Timer();
      totalTime.start();
      loadTime.start();
      Scanner fin = new Scanner(new File("../data/dictionary.txt"));
      Metaphone3 m3 = new Metaphone3();
      while(fin.hasNextLine()==true){//reads from dictionary text file and puts into a dictlist
         
		   String word,phon;
         
		   m3.SetEncodeVowels(true);
		   //m3.SetEncodeExact(true);
         
		   word= fin.nextLine();
		   m3.SetWord(word);
		   m3.Encode();
		   phon = m3.GetMetaph();
         //System.out.println(fin.nextLine());
         dictionary.insert(new DictWord(word,phon));
         totalWords ++;
      }
      loadTime.stop();
      
      //dictionary.display();
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
               if(!dictionary.isInDict(splitted[i])){
                  //System.out.println(splitted[i]);
                  String phon;
                  m3.SetWord(splitted[i]);
		            m3.Encode();
		            phon = m3.GetMetaph();
                  
                  System.out.print("Suggestions for " +splitted[i]+ ": ");
                  dictionary.findPhon(phon);
                  System.out.println();
                  wordsMispelled++;
               }
               
            }
         }  
      }
      parseTime.stop();
      totalTime.stop();
      
      
      System.out.println("Words in Dictionary: "+totalWords);
      System.out.println("Words Checked      : "+wordsChecked);
      System.out.println("Words Not Found    : "+wordsMispelled);
      System.out.println("Time Spent Loading : "+loadTime.seconds() +" seconds");
      System.out.println("Time Spent Parsing : "+parseTime.seconds() +" seconds");
      System.out.println("Total Time Spent   : "+totalTime.seconds() +" seconds");
      
      
      //DictWord testWord = new DictWord("dictionary");
      //System.out.println(testWord.getWord());
      //System.out.println(testWord.getPhon());
      /*
		Metaphone3 m3 = new Metaphone3();
		String word,badword;

		m3.SetEncodeVowels(true);
		//m3.SetEncodeExact(true);

		System.out.print("Enter word: ");
		word= kb.nextLine();

		System.out.print("Enter misspelled word: ");
		badword= kb.nextLine();

		m3.SetWord(word);
		m3.Encode();
		System.out.println(word+" => "+m3.GetMetaph());

		m3.SetWord(badword);
		m3.Encode();
		System.out.println(badword+" => "+m3.GetMetaph());
      */
      
      
	}
}
