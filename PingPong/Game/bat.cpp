#include "Bat.h"
Bat::Bat(float startLocX, float startLocY)
{
    position.x = startLocX;
    position.y = startLocY;
    batShape.setSize(sf::Vector2f(50, 5));
    batShape.setPosition(position);
}
FloatRect Bat::getPosition()
{
    return batShape.getGlobalBounds();
}
RectangleShape Bat::getShape()
{
    return batShape;
}
void Bat::moveLeft()
{
    position.x -= speedBat;
}
void Bat::moveRight()
{
    position.x += speedBat;
}
void Bat::update()
{
    batShape.setPosition(position);
}