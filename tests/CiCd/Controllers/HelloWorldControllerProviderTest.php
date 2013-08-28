<?php
/**
 * This file is part of the cicd-test package.
 *
 * (c) Dries De Peuter <dries@nousefreak.be>
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

namespace CiCd\Controllers;

class HelloWorldControllerProviderTest extends \PHPUnit_Framework_TestCase
{
    public function testConstruct()
    {
        $controller = new HelloWorldControllerProvider();

        $this->assertInstanceOf('\CiCd\Controllers\HelloWorldControllerProvider', $controller);
    }

    public function testFail()
    {
        //$this->assertTrue(false);
    }
}
