// $(function(context){
//     return function(){
//       $('.smallpic').hover(){
//         function(){
//           $('.mainpic').attr('src',this.src)
//         }
//       }
//     }
// }(DMP_CONTEXT.get()))
$(function(context){
        return function(){
            $(".smallpic").hover(
                function(){
                  $(".mainpic").attr('src', this.src)
                }
            )
        }
    }
    (DMP_CONTEXT.get())
);
