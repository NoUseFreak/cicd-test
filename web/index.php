<?php
/**
 * This file is part of the cicd-test package.
 *
 * (c) Dries De Peuter <dries@nousefreak.be>
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

require_once __DIR__.'/../vendor/autoload.php';

$app = new \Silex\Application();

$app->mount('/', new \CiCd\Controllers\HelloWorldControllerProvider());

$app->run();
