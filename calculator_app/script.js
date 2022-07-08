const calculator = document.querySelector('.calculator')
const keys = calculator.querySelector('.calculator__keys')
const display_points = calculator.querySelector('.points')
const display_bails = calculator.querySelector('.bails')

let points_txt="points:"
let bails_txt="bails: "
let last_action=""

let points=new Array(0)
let bails= new Array(0,0,0)

let prev_points=[...points]
let prev_bails=[...bails]

display_points.textContent = points_txt
display_bails.textContent= bails_txt

keys.addEventListener('click', e => {
 if (e.target.matches('button')) {
   const key = e.target
   const action = key.dataset.action
   const key_content = key.textContent
   //let txt=key+"/"+action+"/"+key_content
   //alert(txt)
   

   
   if(action=="add"){
      prev_points=[...points]
      prev_bails=[...bails]
      points.push(parseFloat(key_content))
      last_action="add"
   }else if(action=="bail"){
      prev_points=[...points]
      prev_bails=[...bails]
      
      if(key_content=="-1")
         bails[0]+=1
      else if(key_content=="-2")
         bails[1]+=1
      else
         bails[2]+=1
      last_action="bail"
   }else if(action=="undo"){
      points=[...prev_points]
      bails=[...prev_bails]

   }else if(action=="reset"){
      let isExecuted = confirm("Are you sure you want to reset?")
      if(isExecuted){
         prev_points=[...points]
         prev_bails=[...bails]
         last_action="reset"
         points=new Array(0)
         bails=new Array(0,0,0)
      }
      
   }else if(action=="finalize"){
      prev_points=[...points]
      prev_bails=[...bails]
      
      // sum points
      let sum=0
      for (let i = 0; i < points.length; i++) {
         sum += points[i];
         
      }
      points=[]
      points.push(sum)
      
      last_action="finalize"
   }
      
   //refresh view
   points_txt="points:"+points
   bails_txt="bails:"+bails
   
   display_points.textContent = points_txt
   display_bails.textContent= bails_txt
 
 }
}
)