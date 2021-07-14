/**
* a hsah table centered around phonetic words
*
* @author Austin Leithner
* @version 10/9/19
*
*/
import java.util.*;
import java.io.*;
public class PhonHash extends WordHash{
   PhonHash(String fileName)throws FileNotFoundException{
      super(fileName);
   }
   
   public int hash(DictWord word){
      //return hashA(word.getPhon());
      //return hashB(word.getPhon());
      return hashC(word.getPhon());
   }
}