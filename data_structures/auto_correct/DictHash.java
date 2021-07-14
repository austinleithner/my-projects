/**
* a hsah table centered around dictionary words
*
* @author Austin Leithner
* @version 10/9/19
*
*/
import java.util.*;
import java.io.*;
public class DictHash extends WordHash{
   DictHash(String fileName)throws FileNotFoundException{
      super(fileName);
   }
   
   public int hash(DictWord word){
      //return hashA(word.getWord());
      //return hashB(word.getWord());
      return hashC(word.getWord());
   }
}