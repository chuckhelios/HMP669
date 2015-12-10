/**
*Dashboard
*@namespace root.search.services
*/
(function(){
	'use strict';

	angular
		.module('root.search.services')
		.factory('Search', Search)

	Search.$inject = ['$http', '$rootScope', '$resource','$state', '$stateParams'];

	/**
	* @namespace search
	* @returns {Factory}
	*/
	function Search ($http, $rootScope, $resource, $state ,$stateParams) {
		var Search = {
			SearchResident: SearchResident,
		}

		return Search;

		function SearchResident(){
			console.log($rootScope.$stateParams)
			return $resource('/api/residents/', null, {
				'query': {method: 'GET', isArray:true},
			}).query($rootScope.$stateParams).$promise.then(function(data){
				return data
			});
		}
	}

})();