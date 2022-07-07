// var++ vs ++var
let count = 1;
log(++count,count,count++,count);

// switch (data) {
//      case conditionOfData :
//          do whatever;
//          break;
//      case nextCondition :
//          do another;
//          break;
//      default(the others):
//          do the others;
            
const browser = function (){ return confirm("IE or not?") ? 'IE' : confirm("Firefox or Chrome?") ? 'Chrome' : ''};
switch (browser()) {
    case 'IE':
        log("IE browser!");
        break;
    case 'Chrome':
    case 'Firefox':
        log('Chrome or Firefox browser');
        break;
    default:
        log('not even a browser!');
}

