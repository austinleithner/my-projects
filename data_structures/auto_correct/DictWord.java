/*
* A dictionary word class thats has a word from a dictionary and the phonetic word
*
* @author Austin Leithner
* @version 8/19/19
*
*/
public class DictWord{
   private String word;
   private String phon;
   
   public DictWord(String word,String phon){
      this.word = word;
      this.phon = phon;
   }
   
   /*
   * a getter that returns the word value
   *
   * @return the value of the string word
   */
   public String getWord(){
      return word;
   }
   
   /*
   * a getter that returns the phon value
   *
   * @return the value of the string phon
   */
   public String getPhon(){
      return phon;
   }

}