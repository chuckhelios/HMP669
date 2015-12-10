/**
* em main config
* @name Root Config
* @namespace root.config
* @memberOf root
*/

(function(){
	'use strict';
	angular.module('root.config').config(config);

  /**
  * @name config
  * @desc Enable HTML5 routing
  * @memberOf fcny.config
  */
  function config($locationProvider, $resourceProvider, cfpLoadingBarProvider){
  	$locationProvider.html5Mode(true);
  	$resourceProvider.defaults.stripTrailingSlashes = false;
 	cfpLoadingBarProvider.includeBackdrop = true;

  }	


})();