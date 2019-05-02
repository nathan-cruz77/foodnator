import Vue from 'vue'

var loggedUser = null;

function mockasync (data) {
  return new Promise((resolve, reject) => {
    setTimeout(() => resolve({ data }), 600)
  })
}

const api = {
  login(username, password){
    if(password){
      loggedUser = {
        username: username,
        first_name: 'Mark',
        last_name: 'Zuckerberg',
        email: 'zuck@facebook.com',
        notifications_enabled: true,
        permissions:{
          ADMIN: username == 'admin',
          STAFF: username == 'admin',
        }
      };
    }
    return mockasync(loggedUser);
  },
  logout(){
    loggedUser = null;
    return mockasync({});
  },
  whoami(){
    return mockasync(loggedUser ? {
      authenticated: true,
      user: loggedUser,
    } : {authenticated: false});
  },
  cuisines(){
    return mockasync(['Lanches', 'Brasileira', 'Pizza']);
  },
  updatePreferences(preferences){
    return mockasync({});
  },
};

export default api;
