/*
*driver for binary search tree
*
* @author Austin Leithner
* @version 9/23/19
*
*/
import java.util.*;
import java.io.*;

public class Driver{
   public static void main(String[] args)throws FileNotFoundException{
      Timer totalTime=new Timer();
      totalTime.start();
      MyTree bibleTree=new MyTree("../data/biblewords.txt");
      //bibleTree.printInOrder();
      
      bibleTree.printFirst20();
      //System.out.println(bibleTree.getTotalCount());
      totalTime.stop();
      
      System.out.println();
      System.out.println("Total words: "+bibleTree.getTotalCount());
      System.out.println("Process time: "+bibleTree.getProcessTime()+" seconds");
      System.out.println("Sorting time: "+bibleTree.getSortTime()+" seconds");
      System.out.println("Total time: "+totalTime.seconds()+" seconds");
      
   }
}