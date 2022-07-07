// TO set default params' val 
const showMessage = (message, from = 'unknown') => log(`${message} by ${from}`);
showMessage('hi','jinsoo');
showMessage('hi');

const printAll = (...arr) => log(arr);
printAll = 