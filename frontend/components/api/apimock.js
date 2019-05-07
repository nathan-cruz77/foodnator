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
  groups() {
    return mockasync([
      {name: 'Grupão'},
      {name: 'Treta da neurose'},
      {name: 'Todo mundo null'},
      {name: 'Só no back-end'},
    ])
  },
  updatePreferences(preferences){
    console.log(`pref: ${JSON.stringify(preferences)}`)
    return mockasync({});
  },
  searchUsers(query) {
    return mockasync([
      'Ana',
      'Pedro',
      'Paulo',
      'Maria',
      'Patricia',
      'Lucas',
      'Adriana',
      'Antonia',
      'Joao',
      'Fernanda',
    ]);
  },
  findRestaurant({ name }) {
    return mockasync({ data: `restaurante-bixao-${name}` });
  },
  fetchRestaurant(restaurantSlug) {
    return mockasync({
      name: `Restaurante bixão`,
      slug: restaurantSlug,
      delivery_fee: 7,
      rating: 4.8,
      cuisine: 'Brasileira',
      price_range: 1,
      avatar: 'https://static-images.ifood.com.br/image/upload/f_auto,t_high/logosgde/d939d9aa-8a1c-4d0f-aec1-0024aa1f579c/201901101130_28684.png',
      ifood_url: 'https://www.ifood.com.br/delivery/sao-jose-dos-campos-sp/lig-lig---sao-jose-dos-campos-vila-adyana/a31e0a3a-09c0-4097-a348-4482fd74a3aa'
    });
  },
  newGroup(_) {
    return mockasync('/api/group/new')
  },
};

export default api;
