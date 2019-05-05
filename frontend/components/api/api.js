import axios from '~/helpers/axios';

axios.defaults.xsrfHeaderName = "X-CSRFToken";
axios.defaults.xsrfCookieName = "csrftoken";

const api = {
  login(username, password){
    return post('/api/login', { username, password });
  },
  logout(){
    return post('/api/logout');
  },
  whoami(){
    return get('/api/whoami');
  },
  async cuisines(){
    const { data } = await get('/api/cuisines');
    return data
  },
  groups(username) {
    return get('/api/groups', { username });
  },
  updatePreferences(username, preferences){
    return post('/api/user/preferences', { username, preferences });
  },
  searchUsers(query) {
    return get('/api/users/search', { query });
  },
  findRestaurant(group) {
    return get('/api/find_restaurant', group);
  },
  fetchRestaurant(restaurantSlug) {
    return get(`/api/restaurant/${restaurantSlug}`);
  }
}
export default api;

function get(url, params){
  return axios.get(url, { params });
}

function post(url, params){
  var fd = new FormData();
  params = params || {}
  Object.keys(params).map((k) => {
    fd.append(k, params[k]);
  })
  return axios.post(url, fd);
}
