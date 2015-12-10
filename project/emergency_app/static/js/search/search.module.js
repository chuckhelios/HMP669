/**
* @name search
* @desc initualize app - search
* @namespace root.search
* @memberOf root
*/
(function () {
  'use strict';

  angular
    .module('root.search', [
      'root.search.controllers',
      'root.search.services'
    ]);

  /**
  * @namespace root.search.controllers
  * @memberOf root.search
  */
  angular
    .module('root.search.controllers', []);

  /**
  * @namespace root.search.services
  * @memberOf root.search
  */
  angular
    .module('root.search.services', ['ngCookies']);
})();
