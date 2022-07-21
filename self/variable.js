'use strict';
console.log(`====================  VARIABLE ====================

`)
// The type of  (+- Infinity and NaN) is number 
log(1/0 == Infinity);
log(1/0 == -Infinity);
log(-1/0 == -Infinity);
log(-1/0 == Infinity);
log(typeof(Infinity));
log(typeof(NaN)); // type : num , val : NaN   
log("efe"/2);


// bigint type; greater than 2**53 or less than -(2**53)  

log(3347983249732498743278923487934289734297834298734279843279843342987432987);
log(3347983249732498743278923487934289734297834298734279843279843342987432987n);
log(typeof(3347983249732498743278923487934289734297834298734279843279843342987432987n));


// boolean
// false : 0, null, undefined, NaN , ''
// true : any other val
// null == empty , undefined == not defined


// Symbol                       Symbol(id)
const id = Symbol('id');
const id2 = Symbol('id');
log(id === id2);
log(id == id2);
log(id);
log(id.description);

// Global symbol                Symbol.for(id)
const id3 = Symbol.for('id');
const id4 = Symbol.for('id');
log(id3 == id4);
log(id3 === id4);
log(id3);

// symbol.description           return the symbol key
log(id3.description == id.description);
log(Symbol.for('id').description);
