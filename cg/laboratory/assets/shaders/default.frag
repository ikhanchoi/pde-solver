#version 330 core

uniform sampler2D texture_diffuse1;

// lighting info

in vec2 TexCoords;
layout (location = 0) out vec4 FragColor;

void main()
{
	FragColor = texture(texture_diffuse1, TexCoords);
}