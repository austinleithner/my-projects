/**
 * A linked list of Dictionary words.
 *
 * @author Austin Leithner
 * @version 8/31/19
 *
 */
public class DictList
{
	protected DictNode head;

	/**
	 * A new list has head pointing nowhere.
	 */
	public DictList()
	{
		head= null;
	}


	/**
	 * Displays contents of the list.
	 */
	public void display()
	{
      DictNode p = head;
      while (p != null){
         System.out.println(p.data.getWord());
         p=p.next;
      }
	}


	/**
	 * inserts a dictword into the linked list
	 *
	 * @param newdata The new element to be inserted into the list.
	 */
	public void insert(DictWord newdata)
	{
      DictNode newDictNode = new DictNode();
      newDictNode.data = newdata;
      newDictNode.next = head;
      head  = newDictNode;
	}

   
   /**
	 * Search the list for the value val.
	 *
	 * @param val the value to be searched for
	 * @return true if the string val is in the list
	 */
   
	public boolean isInDict(String val)
	{
      DictNode p = head;
      while (p != null){
         if(p.data.getWord().equals(val)){return true;}
        
         p=p.next;
      }
		return false;
	}
   
   /**
	 * Search the list for all matching phon values and prints the word associated with it.
	 *
	 * @param phon the value to be searched for
	 * 
	 */
   
	public void findPhon(String phon)
	{
      DictNode p = head;
      while (p != null){
         if(p.data.getPhon().equals(phon)){System.out.print(p.data.getWord()+" ");}
         
         p=p.next;
      }
		
	}
}
