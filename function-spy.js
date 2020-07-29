
function attach(level){
  for (var key in level) {
      // check if the property/key is defined in the object itself, not in parent
      if (level.hasOwnProperty(key) && key !="attach") {     
          var value = level[key]
          if (typeof value == "function"){
              level[key]=function(){
                      value.apply(this,arguments)
                    }
          }
      }
  }
  return level
}

window = attach(window)
