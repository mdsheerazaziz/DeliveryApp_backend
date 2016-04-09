var app = angular.module('DeliveryApp', [ 'ngRoute', 'ngMaterial' ])

app.config([
				'$httpProvider',
				function($httpProvider) {
					$httpProvider.defaults.xsrfCookieName = 'csrftoken';
					$httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
					$httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8';

				} ]);

app.config(function($interpolateProvider) {
	$interpolateProvider.startSymbol('[[');
	$interpolateProvider.endSymbol(']]');
});
app.controller(
				'IndexController',
				function DemoCtrl($scope) {

				});