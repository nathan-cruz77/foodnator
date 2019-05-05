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
  groups(username) {
    return mockasync([
      {name: `Grupão de "${username}"`},
      {name: 'Treta da neurose'},
      {name: 'Todo mundo null'},
      {name: 'Só no back-end'},
    ])
  },
  updatePreferences(preferences){
    return mockasync({});
  },
  searchUsers(query) {
    return mockasync([
      { id: 0, username: 'Ana' },
      { id: 1, username: 'Pedro' },
      { id: 2, username: 'Paulo' },
      { id: 3, username: 'Maria' },
      { id: 4, username: 'Patricia' },
      { id: 5, username: 'Lucas' },
      { id: 6, username: 'Adriana' },
      { id: 7, username: 'Antonia' },
      { id: 8, username: 'Joao' },
      { id: 9, username: 'Fernanda' },
    ]);
  },
  findRestaurant({ name }) {
    return mockasync(`restaurante-bixao-${name}`);
  },
  fetchRestaurant(restaurantSlug) {
    return mockasync({
      name: `Restaurante bixão`,
      slug: restaurantSlug,
      delivery_fee: 7,
      rating: 4.8,
      cuisine: 'Brasileira',
      price_range: 'CHEAPEST',
    });
  }
};

export default api;
