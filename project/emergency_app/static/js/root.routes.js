/**
* em main routes
* @name em routes
* @namespace root.routes
* @memberOf root
*/
(function () {
  'use strict';
  angular.module('root.routes').config(config);

  config.$inject = ['$stateProvider' , '$urlRouterProvider'];

  /**
  * @name routes
  * @desc Define valid application routes
  * @memberOf root.routes
  */
  function config($stateProvider, $urlRouterProvider){
    // For any unmatched url, send to /login
    $urlRouterProvider.otherwise("/");
  	$stateProvider.state('login', {
  		url: '/login',
  		views: {
  			'ui-top-view': {
  				templateUrl: '/static/templates/authentication/login.html',
  				controller: 'LoginController as vm'
  			}
  		}
  	}).state('index', {
      url: '/',
      views:{
        'ui-top-view':{
          templateUrl: '/static/templates/com/index.html',
          controller: 'SearchController as vm'
        }
      }
    }).state('resident', {
      abstract: true,
      url: '/resident', 
      resolve: {
        residents : ['Search', function(Search){
          return Search.SearchResident();
        }]
        // gender: ['$stateParams', function($stateParams){
        //   return $stateParams
        // }]
      },
      views:{
        'ui-top-view':{
          templateUrl:'/static/templates/search/resident.html',
          controller: 'ResidentController as vm'
        }
      }
    }).state('resident.list', {
      url: '',
      templateUrl: '/static/templates/search/resident.list.html',
      controller: 'ResidentListController as vm'
    }).state('resident.detail', {
      url: '/{mrn}',
      views:{
        'resident-detail': {
          templateUrl: '/static/templates/search/resident.detail.html',
          controller: 'ResidentDetailController as vm'
        }
      }
    });//end state
  
  }


})();