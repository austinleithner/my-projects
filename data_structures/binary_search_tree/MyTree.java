/*
* A binary search tree
*
* @author Austin Leithner
* @version 9/13/19
*
*/

import java.io.*;
import java.util.*;

public class MyTree{
   private TreeNode root;
   private int totalCount=0;
   private int pos=0;
   private TreeNode[] a;
   private Timer processTime= new Timer();
   private Timer sortTime= new Timer();
   
   public MyTree(String fileName)throws FileNotFoundException{
      Scanner fin = new Scanner(new File(fileName));
      processTime.start();
      
      while(fin.hasNextLine()){
         String tempdata = fin.nextLine();
         TreeNode temptn = search(tempdata);
         
         if(temptn!=null){
            temptn.data.count++;
         }else{
            insert(tempdata);
            totalCount++;
         }
         
      }
      processTime.stop();
      a= new TreeNode[totalCount];
      fillArray();
      sortTime.start();
      sort();
      sortTime.stop();
      
   }
   
   /*
   * a getter for the process time
   *
   * @return double the seconds for the process time
   *
   */
   public double getProcessTime(){
      return processTime.seconds();
   }
   
   /*
   * a getter for the sort time
   *
   * @return double the seconds for the sort time
   *
   */
   public double getSortTime(){
      return sortTime.seconds();
   }
   
   /*
   * traverses the tree starting at the given node and prints out in order
   *
   * @param node the node to start the traversal
   *
   *
   */
   public void inOrder(TreeNode node){
      if(node != null){
         inOrder(node.left);
         System.out.print(node.data.word+":");
         System.out.println(node.data.count+1);
         inOrder(node.right);
      }
   }
   
   /*
   * prints out list in order
   *
   *
   *
   */
   public void printInOrder(){
      inOrder(root);
   }
   
   /*
   * searches the tree for the given data
   *
   * @param data the data to be search for
   * @return returns a TreeNode where the data is
   *
   */
   public TreeNode search(String data){
      
      TreeNode p=root;
      
      while(p != null && !(p.data.compareTo(data)==0)){
         
         if(p.data.compareTo(data)<0){
            p=p.right;
         }else{
            p=p.left;
         }
      }
      return p;
   }
   
   /*
   * inserts a string into the tree
   *
   * @param data the string data to be inserted
   *
   *
   */
   public void insert(String data){
      TreeNode nn, p, q;
      nn= new TreeNode();
      nn.data=new Word();
      nn.data.word= data;//java.lang.NullPointerException fixed had to init new Word()
      nn.left=null;
      nn.right=null;
      
      p=root;
      q=null;
      while(p!=null){
         q=p;
         if(data.compareTo(p.data.word)<0){
            p=p.left;
         }else{
            p=p.right;
         }
      }
   
      if(q==null){root=nn;}
      else{
         if(data.compareTo(q.data.word)<0){
            q.left=nn;
         }else{
            q.right=nn;
         }
      }
   
   }
   
   /*
   * a getter for the total count varible
   *
   * @return int the value of the total count varible
   *
   */
   public int getTotalCount(){
      return totalCount;
   }
   
   /*
   *
   *method that calls the method to fill the array
   *
   *
   */
   public void fillArray(){
      traverseArray(root);
   }
   
   /*
   *
   *fills the array with the tree elements
   *
   * @param node the starting node
   */
   public void traverseArray(TreeNode node){
      if(node != null){
         traverseArray(node.left);
         addToArray(node);
         //System.out.print(node.data.word+":");
         //System.out.println(node.data.count+1);
         traverseArray(node.right);
      }
   }
   
   /*
   *
   * adds treenode to array
   *
   * @param data the treenode to be added to the array
   */
   public void addToArray(TreeNode data){
      if(pos<totalCount){
         a[pos]= data;
         pos++;
      }
   }
   
   /*
   *
   *prints the array
   *
   *
   */
   public void printArray(){
      //System.out.println(Arrays.toString(a));
      for(int i =0;i<totalCount;i++){
         System.out.println(a[i].data.word+":"+a[i].data.count);
      }
   }
   
   /*
   *
   *prints the first 20 elems of the array
   *
   *
   */
   public void printFirst20(){
      //System.out.println(Arrays.toString(a));
      for(int i =0;i<20;i++){
         System.out.println(a[i].data.word+":"+a[i].data.count);
      }
   }
   
   /**
   *
   * A container for the quicksort method
   *
   *
   */
   private void sort(){
      qsort(a,0,totalCount-1);
   }
   
   /**
   * the quicksort method
   *
   * @param tn a treenode array
   * @param p the lower pointer
   * @param r the upper pointer
   *
   */
   private void qsort(TreeNode[] tn, int p, int r){
      if(p<r){
         int q = partition(tn,p,r);
         qsort(tn,p,q);
         qsort(tn,q+1,r);
      }
   }
   
   /**
   * partitions the given array and is the backbone of the qsort method
   *
   * @param tn a treenode array
   * @param p the lower pointer
   * @param r the upper pointer
   * @return int returns the array position of the partition
   */
   private int partition(TreeNode[] tn,int p, int r){
      TreeNode k,temp;
      int i,j;
      
      
      j=r+1;
      i=p-1;
      k=tn[p];
      do{
         do{j--;}while(tn[j].data.count<k.data.count);
         do{i++;}while(tn[i].data.count>k.data.count);
         if(i<j)//i<j words[i].compareTo(words[j])<0
         {
            temp = a[i];
            a[i]=a[j];
            a[j]=temp;
         }
      }while(i<j);
      
      return j;
   }
}