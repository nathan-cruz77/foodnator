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
  cuisines(){
    return get('/api/cuisines');
  },
  updatePreferences(preferences){
    return null;
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
