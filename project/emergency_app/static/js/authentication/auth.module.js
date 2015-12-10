/**
* @name authentication
* @desc initualize app - authentication
* @namespace root.authentication
* @memberOf root
*/
(function () {
  'use strict';

  angular
    .module('root.authentication', [
      'root.authentication.controllers',
      'root.authentication.services'
    ]);

  /**
  * @namespace root.authentication.controllers
  * @memberOf root.authentication
  */
  angular
    .module('root.authentication.controllers', []);

  /**
  * @namespace root.authentication.services
  * @memberOf root.authentication
  */
  angular
    .module('root.authentication.services', ['ngCookies']);
})();
