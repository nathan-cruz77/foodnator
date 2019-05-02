import AppApi from '~apijs'

export default function ({ store }) {
  if(!store.state.user.loggedUser){
    return AppApi.whoami().then(({ data }) => {
      if(data.authenticated){
        store.commit('user/setLoggedUser', data.user)
      } else {
        store.commit('user/setLoggedUser', null)
      }
    });
  }
}
