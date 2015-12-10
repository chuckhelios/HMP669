/**
* emergency_app
* @name em App
* @namespace root
*/
(function(){
  // body...
  'use strict';
  angular.module('root', [
      'root.injectCom',
      'root.routes',
      'root.config',
      'root.authentication',
      'root.search',
      
    ]);


  angular.module('root.injectCom', [
        'ngAnimate',
        'ngResource',
        'ngSanitize',
        'angular-blocks',        
        'ui.router',
        'ui.utils',
        'mgcrea.ngStrap',
        'ui.bootstrap',
        'restangular',
        'base64',
        'ngCookies',
        'vButton',
        'ngTagsInput',
        'angular-loading-bar',
      ]);


  angular.module('root.routes', ['ngRoute']);
  angular.module('root.config', []);

  angular.module('root').run(run);

  run.$inject = ['$rootScope', '$location', '$cookieStore', '$http', '$state', '$stateParams',];

  /**
  * @name run
  * @desc Update xsrf $http headers to align with Django's defaults
  * @memberOf fcny
  */
  function run($rootScope, $location, $cookieStore, $http,  $state, $stateParams) {
    
    $rootScope.$state = $state;
    $rootScope.$stateParams = $stateParams;
    // keep user logged in after page refresh
    $rootScope.globals = $cookieStore.get('globals') || {};
    if ($rootScope.globals.currentUser) {
      $http.defaults.headers.common['Authorization'] = 'Basic ' + $rootScope.globals.currentUser.authdata; // jshint ignore:line
    }
    $rootScope.$on('$locationChangeStart', function (event, next, current) {
        // redirect to login page if not logged in
        if ($location.path() !== '/login' && !$rootScope.globals.currentUser) {
          $location.path('/login');
          $state.go('login');
        }
    });

    $http.defaults.xsrfHeaderName = 'X-CSRFToken';
    $http.defaults.xsrfCookieName = 'csrftoken';

  }


})();