#include "Ball.h"
Ball::Ball(float startLocX, float startLocY)
{
    position.x = startLocX;
    position.y = startLocY;
    ballShape.setSize(sf::Vector2f(10, 10));
    ballShape.setPosition(position);
}
FloatRect Ball::getPosition()
{
    return ballShape.getGlobalBounds();
}
RectangleShape Ball::getShape()
{
    return ballShape;
}
float Ball::getXVelocity()
{
    return velocityX;
}
void Ball::reboundSides()
{
    velocityX = -velocityX;
}
void Ball::reboundBatOrTop()
{
    position.y -= (velocityY * 30);
    velocityY = -velocityY;
 
}
void Ball::hitBottom()
{
    position.y = 1;
    position.x = 500;
}
void Ball::update()
{
    position.y += velocityY;
    position.x += velocityX;
    ballShape.setPosition(position);
}