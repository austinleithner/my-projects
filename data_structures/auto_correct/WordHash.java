/**
* an abstract hash table class
*
*
* @author Austin Leithner
* @version 10/9/19
*/
import java.util.*;
import java.io.*;
public abstract class WordHash{
   
   DictNode[] table;
   int totalWords;
   
   WordHash(String filename)throws FileNotFoundException{
      Scanner fin = new Scanner(new File(filename));
      Metaphone3 m3 = new Metaphone3();
      table=new DictNode[500000];
      while(fin.hasNextLine()==true){//reads from dictionary text file and puts into a dictlist
         
		   String word,phon;
         
		   m3.SetEncodeVowels(true);
		   //m3.SetEncodeExact(true);
         
		   word= fin.nextLine();
		   m3.SetWord(word);
		   m3.Encode();
		   phon = m3.GetMetaph();
         DictNode tempNode = new DictNode();
         tempNode.data = new DictWord(word,phon);
         //System.out.println(fin.nextLine());
         add(tempNode);
         totalWords ++;
      }
   }
   /**
   * abstract hash for dictwords
   *
   * @param s string to be hashed
   * @return an int which represents the hash value of the string
   *
   */
   public abstract int hash(DictWord word);
   
   /**
   * java hashcode
   *
   * @param s string to be hashed
   * @return an int which represents the hash value of the string
   *
   *
   */
   public int hashA(String s){
      return Math.abs(s.hashCode())%table.length;
   }
   
   /**
   * in class hash
   *
   * @param s string to be hashed
   * @return an int which represents the hash value of the string
   *
   */
   public int hashB(String s){
      int val= 1;
      for(int i=0; i<s.length();i++){
         val= val * (int)s.charAt(i);
      }
      return Math.abs(val)%table.length;
   }
   
   /**
   * custom made hash function
   *
   * @param s string to be hashed
   * @return an int which represents the hash value of the string
   *
   */
   public int hashC(String s){
      int val= 7;
      for(int i=0; i<s.length();i++){
         val= (val*31) + (int)s.charAt(i);
      }
      return Math.abs(val)%table.length;
   }
   /**
   * adds a dictnode to the hash table
   *
   * @param node the node to be added
   *
   */
   public void add(DictNode node){
      int pos = hash(node.data);
      DictNode newDictNode = node;
      //newDictNode.data = node.data;
      newDictNode.next = table[pos];
      table[pos] = newDictNode;
   }
   
   /**
   *searches the table to see if the dictnode word value is in the table
   *
   * @param node the dictnode to be searched for
   * @return DictWord with the matching word value
   */
   public DictWord searchWord(DictNode node){
      int pos = hash(node.data);
      DictNode p = table[pos];
      while (p != null){
         if(p.data.getWord()==node.data.getWord()){
            return p.data;
         }
         p=p.next;
      }
      return p.data;
   }
   
   /**
   *searches the table to see if the dictnode phon value is in the table
   *
   * @param node the dictnode to be searched for
   * @return DictWord with the matching phon value
   */
   public DictWord searchPhon(DictNode node){
      int pos = hash(node.data);
      DictNode p = table[pos];
      while (p != null){
         if(p.data.getPhon()==node.data.getPhon()){
            return p.data;
         }
         p=p.next;
      }
      return p.data;
   }
   
   /**
   *prints all words that matches the phon
   *
   * @param word a dictword
   *
   */
   public void findPhon(DictWord word){
      int pos = hash(word);
      if(table[pos]!=null){
         DictNode p = table[pos];
         while (p != null){
            if(p.data.getPhon().equals(word.getPhon())){System.out.print(p.data.getWord()+" ");}
         
            p=p.next;
         }
      }
   }
   /**
   *checks if the dictword in in the hash table
   *
   * @param word a dictword to be checked
   * @return true if dictword is in hash table false if not
   *
   */
   public boolean isInDict(DictWord word){
      int pos = hash(word);
      if(table[pos]!=null){
         DictNode p = table[pos];
         while (p != null){
            if(p.data.getWord().equals(word.getWord())){return true;}
         
            p=p.next;
         }
         
      }
      return false;
   }
   /**
   * a getter for total words
   *
   * @return totalWords
   *
   */
   public int getTotalWords(){return totalWords;}
   
   /**
   *counts the total elems in the table hash
   *
   * @return the total elem count
   *
   */
   public int totalElems(){
     int elemcnt = 0;
     for(int i = 0; i< table.length; i++){
       if(table[i]!=null){
          elemcnt++;
       }
     }
     return elemcnt;
   }
   /**
   * counts the longest list
   *
   * @return the longest list size
   */
    public int longestList(){
      int totalcnt=0;
      for(int i = 0; i< table.length; i++){
         DictNode p = table[i];
         int tempcnt = 0;
         while(p!=null){
            tempcnt++;
            p=p.next;
            //elemcnt++;
         }
         if(tempcnt>totalcnt){totalcnt=tempcnt;}
      }
      return totalcnt;
   }
}