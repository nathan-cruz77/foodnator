import Vue from 'vue'

var logged_user = null;

function mockasync (data) {
  return new Promise((resolve, reject) => {
    setTimeout(() => resolve({ data }), 600)
  })
}

const api = {
  login(username, password){
    if(password){
      logged_user = {
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
    return mockasync(logged_user);
  },
  logout(){
    logged_user = null;
    return mockasync({});
  },
  whoami(){
    return mockasync(logged_user ? {
      authenticated: true,
      user: logged_user,
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
