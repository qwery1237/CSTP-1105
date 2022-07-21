'use strict';
console.clear();
class UserStorage {
    loginUser(id, password, onSuccess, onError){
        setTimeout(()=> {
            if (
                (id === 'jinsoo' && password === 'son') ||
                (id === 'yu' && password === 'hatoyama')
                ) {
                    onSuccess(id);
                } else {
                    onError(new Error('not found'));
                }
        },2000)
    }
    getRoles(user, onSuccess, onError){
        setTimeout(() => {
            if (user === 'jinsoo') {
                onSuccess({name: 'jinsoo', role: 'admin'});
            } else {
                onError(new Error('no access'));
            }
        }, 1000);
    }
}
const userStorage = new UserStorage();
const id15 = prompt('id');
const password = prompt('password');
userStorage.loginUser(
    id15,
    password,
    user => {
        userStorage.getRoles(
            user,
            userWithRole => {
                alert(`Hello ${userWithRole.name}, you have a ${userWithRole.role} role`)
            },
            error => {
                console.log(error);
            }
        )
    },
    error => {
        console.log(error);
    }
    );